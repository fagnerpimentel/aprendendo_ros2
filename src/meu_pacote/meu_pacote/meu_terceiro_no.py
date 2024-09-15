import rclpy # type: ignore
from rclpy.node import Node # type: ignore

# Cria o nó do ROS como uma clase do python
class MeuNo(Node):

    # Contrutor do nó
    def __init__(self):
        # Aqui é definido o nome do nó
        super().__init__('meu_terceiro_no')

    # Aqui o seu nó está executando no ROS
    def run(self):
        self.get_logger().info('Parabéns, você criou o seu primeiro nó com classe!')

        self.get_logger().debug ('Exemplo de mensagem de debug nó com classe.')
        self.get_logger().info  ('Exemplo de mensagem de informação nó com classe.')
        self.get_logger().warn  ('Exemplo de mensagem de aviso nó com classe.')
        self.get_logger().error ('Exemplo de mensagem de erro comum nó com classe.')
        self.get_logger().fatal ('Exemplo de mensagem de erro fatal nó com classe.')

        # Executa uma iteração do loop de processamento de mensagens.
        rclpy.spin_once(self)

    # Destrutor do nó
    def __del__(self):
        self.get_logger().info('Finalizando o nó com classe! Tchau, tchau...')


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
