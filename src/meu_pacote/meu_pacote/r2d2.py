import rclpy  # type: ignore
from rclpy.node import Node # type: ignore

from sensor_msgs.msg import LaserScan # type: ignore
from nav_msgs.msg import Odometry # type: ignore
from geometry_msgs.msg import Twist, Vector3 # type: ignore

from rclpy.qos import QoSProfile, QoSReliabilityPolicy # type: ignore

from tf2_ros import TransformException # type: ignore
from tf2_ros.buffer import Buffer # type: ignore
from tf2_ros.transform_listener import TransformListener # type: ignore
import tf_transformations # type: ignore

from math import sqrt, pi, exp

class R2D2(Node):

    def __init__(self):
        super().__init__('R2D2')

        # variables and constants
        raio = 0.02
        distancia_rodas = 0.4
        pose = [0, 0, 0] # x, y, theta
        medidas = [0, 0] # esq, dir
        ultimas_medidas = [0, 0] # esq, dir
        distancias = [0, 0]

        # mapa
        estado_inicial = 0
        mapa = [1.5, 4.5] # posição central das três “portas” existentes
        pose[0] = estado_inicial # atualiza como estado_inicial a posição x de pose

        # sigma
        sigma_odometria = 0.2 # rad
        sigma_lidar = 0.175 # meters
        sigma_movimento = 0.002 # m
        
        def gaussian(x, mean, sigma):
            return (1 / (sigma*sqrt(2*pi))) * exp(-((x-mean)**2) / (2*sigma**2))

        # update function
        def update():
            medidas[0] = left_encoder.getValue()
            medidas[1] = right_encoder.getValue()
            diff = medidas[0] - ultimas_medidas[0] # conta quanto a roda LEFT girou desde a última medida (rad)
            distancias[0] = diff * raio + random.normal(0,0.002) # determina distância percorrida em metros e adiciona um pequeno erro

            ultimas_medidas[0] = medidas[0]
            diff = medidas[1] - ultimas_medidas[1] # conta quanto a roda LEFT girou desde a última medida (rad)
            distancias[1] = diff * raio + random.normal(0,0.002) # determina distância percorrida em metros + pequeno erro
            ultimas_medidas[1] = medidas[1]
            # ## cálculo da dist linear e angular percorrida no timestep
            deltaS = (distancias[0] + distancias[1]) / 2.0
            deltaTheta = (distancias[1] - distancias[0]) / distancia_rodas
            pose[2] = (pose[2] + deltaTheta) % 6.28 # atualiza o valor Theta (diferença da divisão por 2π)

            # decomposição x e y baseado no ângulo
            deltaSx = deltaS * cos(pose[2])
            deltaSy = deltaS * sin(pose[2])

            # atualização acumulativa da posição x e y
            pose[0] = pose[0] + deltaSx # atualiza x
            pose[1] = pose[1] + deltaSy # atualiza y

            print("Postura:", pose)

        self.get_logger().debug ('Definido o nome do nó para "R2D2"')

        qos_profile = QoSProfile(depth=10, reliability = QoSReliabilityPolicy.BEST_EFFORT)

        self.get_logger().debug ('Definindo o subscriber do laser: "/scan"')
        self.laser = None
        self.create_subscription(LaserScan, '/scan', self.listener_callback_laser, qos_profile)

        self.get_logger().debug ('Definindo o subscriber do laser: "/odom"')
        self.pose = None
        self.create_subscription(Odometry, '/odom', self.listener_callback_odom, qos_profile)

        self.get_logger().debug ('Definindo o publisher de controle do robo: "/cmd_Vel"')
        self.pub_cmd_vel = self.create_publisher(Twist, '/cmd_vel', 10)

        self.get_logger().info ('Definindo buffer, listener e timer para acessar as TFs.')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(0.1, self.on_timer)

    def listener_callback_laser(self, msg):
        self.laser = msg.ranges
       
    def listener_callback_odom(self, msg):
        self.pose = msg.pose.pose

    def on_timer(self):
        try:
            self.tf_right = self.tf_buffer.lookup_transform(
                "right_center_wheel",
                "right_leg_base",
                rclpy.time.Time())

            _, _, self.right_yaw = tf_transformations.euler_from_quaternion(
                [self.tf_right.transform.rotation.x, self.tf_right.transform.rotation.y, 
                self.tf_right.transform.rotation.z, self.tf_right.transform.rotation.w]) 

            self.get_logger().info (
                f'yaw right_leg_base to right_center_wheel: {self.right_yaw}')

        except TransformException as ex:
            self.get_logger().info(
            f'Could not transform right_leg_base to right_center_wheel: {ex}')
        
        
        try:
            self.tf_left = self.tf_buffer.lookup_transform(
                "left_center_wheel",
                "left_leg_base",
                rclpy.time.Time())

            _, _, self.left_yaw = tf_transformations.euler_from_quaternion(
                [self.tf_left.transform.rotation.x, self.tf_left.transform.rotation.y, 
                self.tf_left.transform.rotation.z, self.tf_left.transform.rotation.w]) 

            self.get_logger().info (
                f'yaw left_leg_base to left_center_wheel: {self.left_yaw}')

        except TransformException as ex:
            self.get_logger().info(
            f'Could not transform left_leg_base to left_center_wheel: {ex}')






    def run(self):
         
        self.get_logger().debug ('Executando uma iteração do loop de processamento de mensagens.')
        rclpy.spin_once(self)

        self.get_logger().debug ('Definindo mensagens de controde do robô.')
        self.ir_para_frente = Twist(linear=Vector3(x= 0.5,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z= 0.0))
        self.parar          = Twist(linear=Vector3(x= 0.0,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z= 0.0))

        self.get_logger().info ('Ordenando o robô: "ir para a frente"')
        self.pub_cmd_vel.publish(self.ir_para_frente)
        rclpy.spin_once(self)

        self.get_logger().info ('Entrando no loop princial do nó.')
        while(rclpy.ok):
            rclpy.spin_once(self)

            self.get_logger().debug ('Atualizando as distancias lidas pelo laser.')
            self.distancia_direita   = min((self.laser[  0: 80])) # -90 a -10 graus
            self.distancia_frente    = min((self.laser[ 80:100])) # -10 a  10 graus
            self.distancia_esquerda  = min((self.laser[100:180])) #  10 a  90 graus

            self.get_logger().debug ("Distância para o obstáculo" + str(self.distancia_frente))
            if(self.distancia_frente < 1.5):
                self.get_logger().info ('Obstáculo detectado.')
                break

        self.get_logger().info ('Ordenando o robô: "parar"')
        self.pub_cmd_vel.publish(self.parar)
        rclpy.spin_once(self)


    # Destrutor do nó
    def __del__(self):
        self.get_logger().info('Finalizando o nó! Tchau, tchau...')


# Função principal
def main(args=None):
    rclpy.init(args=args)
    node = R2D2()
    try:
        node.run()
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass
   
if __name__ == '__main__':
    main()  

