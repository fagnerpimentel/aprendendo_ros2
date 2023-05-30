import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity

def main(args=None):
    # Inicializa o processo
    rclpy.init(args=args)
    
    # Controi o nó
    node = Node('no_simples')

    # # Define o nível do logger
    # logger = node.get_logger()
    # logger.set_level(LoggingSeverity.INFO)

    # Algumas impressões e exemplos de uso do logger
    node.get_logger().info('Parabéns, você criou o seu primeiro nó!')
    node.get_logger().debug ('Exemplo de mensagem de debug.')
    node.get_logger().info  ('Exemplo de mensagem de informação.')
    node.get_logger().warn  ('Exemplo de mensagem de aviso.')
    node.get_logger().error ('Exemplo de mensagem de erro comum.')
    node.get_logger().fatal ('Exemplo de mensagem de erro fatal.')
    node.get_logger().info('Finalizando o nó! Tchau, tchau...')

    # Destroi o nó 
    node.destroy_node()

    # Finaliza o processo
    rclpy.shutdown()


if __name__ == '__main__':
    main()    




