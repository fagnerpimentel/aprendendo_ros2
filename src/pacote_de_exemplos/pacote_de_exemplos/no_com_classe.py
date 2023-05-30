import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity
# Cria o nó do ROS como uma clase do python
class MeuNo(Node):

    # Contrutor do nó
    def __init__(self):
        # Aqui é definido o nome do nó
        super().__init__('no_com_classe')

        # # Define o nível do logger
        # logger = self.get_logger()
        # logger.set_level(LoggingSeverity.INFO)

    # Aqui o seu nó está executando no ROS
    def run(self):
        self.get_logger().info('Parabéns, você criou o seu primeiro nó!')

        self.get_logger().debug ('Exemplo de mensagem de debug.')
        self.get_logger().info  ('Exemplo de mensagem de informação.')
        self.get_logger().warn  ('Exemplo de mensagem de aviso.')
        self.get_logger().error ('Exemplo de mensagem de erro comum.')
        self.get_logger().fatal ('Exemplo de mensagem de erro fatal.')

        # Executa uma iteração do loop de processamento de mensagens.
        rclpy.spin_once(self)

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




