import rclpy # type: ignore
from rclpy.node import Node # type: ignore
from rclpy.logging import LoggingSeverity # type: ignore

def main(args=None):
    # Inicializa o processo
    rclpy.init(args=args)
    
    # Controi o nó
    node = Node('no_simples')

    # # Define o nível do logger
    # logger = node.get_logger()
    # logger.set_level(LoggingSeverity.INFO)

    # Algumas impressões e exemplos de uso do logger
    node.get_logger().info('Parabéns, você criou o seu segundo nó!')
    node.get_logger().debug ('Exemplo de mensagem de debug do segundo nó.')
    node.get_logger().info  ('Exemplo de mensagem de informação do segundo nó.')
    node.get_logger().warn  ('Exemplo de mensagem de aviso do segundo nó.')
    node.get_logger().error ('Exemplo de mensagem de erro comum do segundo nó.')
    node.get_logger().fatal ('Exemplo de mensagem de erro fatal do segundo nó.')
    node.get_logger().info('Finalizando o do segundo nó! Tchau, tchau...')

    # Destroi o nó 
    node.destroy_node()

    # Finaliza o processo
    rclpy.shutdown()


if __name__ == '__main__':
    main()    
