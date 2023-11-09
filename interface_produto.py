import tkinter as tk
import crud as crud
import psycopg2

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()

        # Componentes da interface de usuário
        self.lbCodigo = tk.Label(win, text='Código do Produto:')
        self.lblNome = tk.Label(win, text='Nome do Produto')
        self.lblPreco = tk.Label(win, text='Preço')
        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)

        # Posicione os componentes
        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)
        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)
        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)
        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

    def fCadastrarProduto(self):
        try:
            # Ler os valores dos campos
            codigo, nome, preco = self.fLerCampos()

            # Chamar o método de inserção de dados no objeto self.objBD
            self.objBD.inserirDados(codigo, nome, preco)

            # Limpar os campos da tela após o cadastro
            self.fLimparTela()

            # Imprimir uma mensagem de sucesso
            print('Produto Cadastrado com Sucesso!')

        except Exception as e:
            # Capturar exceções e imprimir uma mensagem de erro
            print('Não foi possível fazer o cadastro. Erro:', e)

    def fAtualizarProduto(self):
        try:
            # Ler os valores dos campos
            codigo, nome, preco = self.fLerCampos()

            # Chamar o método de atualização de dados no objeto self.objBD
            self.objBD.atualizarDados(codigo, nome, preco)

            # Limpar os campos da tela após a atualização
            self.fLimparTela()

            # Imprimir uma mensagem de sucesso
            print('Produto Atualizado com Sucesso!')

        except Exception as e:
            # Capturar exceções e imprimir uma mensagem de erro
            print('Não foi possível fazer a atualização. Erro:', e)

    def fExcluirProduto(self):
        try:
            # Ler os valores dos campos
            codigo, nome, preco = self.fLerCampos()

            # Chamar o método de exclusão de dados no objeto self.objBD
            self.objBD.excluirDados(codigo)

            # Limpar os campos da tela após a exclusão
            self.fLimparTela()

            # Imprimir uma mensagem de sucesso
            print('Produto Excluído com Sucesso!')

        except Exception as e:
            # Capturar exceções e imprimir uma mensagem de erro
            print('Não foi possível fazer a exclusão do produto. Erro:', e)

    def fLimparTela(self):
        try:
            # Limpa os campos de entrada
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print('Campos Limpos!')

        except Exception as e:
            # Capturar exceções e imprimir uma mensagem de erro
            print('Não foi possível limpar os campos. Erro:', e)

    def fLerCampos(self):
        # Implemente a lógica para ler os valores dos campos
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        return codigo, nome, preco

# Inicialização da interface
if __name__ == "__main__":
    janela = tk.Tk()
    principal = PrincipalBD(janela)
    janela.title('Bem Vindo a Tela de Cadastro')
    janela.geometry("600x500")
    janela.mainloop()
