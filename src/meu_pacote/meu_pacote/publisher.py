import rclpy # type: ignore
from rclpy.node import Node # type: ignore
from std_msgs.msg import String # type: ignore

class MeuNo(Node):

    # Contrutor do nó
    def __init__(self):

        # Aqui é definido o nome do nó
        super().__init__('publisher')

        self.get_logger().info('Definindo meu primeiro publisher!')
        self.publisher = self.create_publisher(String, 'meu_topico', 10)

    # Aqui o nó é executado no ROS
    def run(self):


        self.get_logger().info('Publicando mensagem a cada um segundo!')
        timer = self.create_timer(1, self.talker_callback)

        # Executa uma iteração do loop de processamento de mensagens.
        rclpy.spin(self)

    # funcção de callback que publica a mensagem
    def talker_callback(self):
        msg = String()
        msg.data = 'Isso é uma mensagem!'
        self.publisher.publish(msg)

    # Destrutor do nó
    def __del__(self):
        self.get_logger().info('Finalizando o publisher! Tchau, tchau...')


# Função principal
def main(args=None):
    rclpy.init(args=args)
    node = MeuNo()
    try:
        node.run()
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass
   
if __name__ == '__main__':
    main()
