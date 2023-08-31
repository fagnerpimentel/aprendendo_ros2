import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MeuNo(Node):

    # Contrutor do nó
    def __init__(self):

        # Aqui é definido o nome do nó
        super().__init__('listener')

        self.get_logger().info('Definindo meu primeiro subscriber!')
        self.subscription = self.create_subscription(String,'meu_topico',self.listener_callback,10)
        
    # Aqui o nó é executado no ROS
    def run(self):

        # Executa uma iteração do loop de processamento de mensagens.
        rclpy.spin(self)

    # funcção de callback que lê a mensagem
    def listener_callback(self, msg):
        self.get_logger().info('Mensagem publicada: "%s"' % msg.data)

    # Destrutor do nó
    def __del__(self):
        self.get_logger().info('Finalizando o nó! Tchau, tchau...')


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