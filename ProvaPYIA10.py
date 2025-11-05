import re
import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.START

    nome = ft.TextField(label="Nome", width=450)
    email = ft.TextField(label="Email", width=450)
    mensagem = ft.TextField(label="Mensagem", multiline=True, min_lines=4, width=450)

    # Texto de status para confirmação final exibida na tela
    status_confirmacao = ft.Text("", color="green")

    def mostrar_confirmacao():
        """Define a mensagem de confirmação visível na tela com timestamp."""
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status_confirmacao.value = f"Formulário enviado com sucesso em {ts}."
        page.update()

    def fechar_dialog(ev):
        if page.dialog:
            page.dialog.open = False
        # mostra mensagem de confirmação final com timestamp (usa função comum)
        mostrar_confirmacao()
        # limpa campos após fechar (garantia)
        nome.value = ""
        email.value = ""
        mensagem.value = ""
        page.update()

    def enviar(ev):
        n = nome.value.strip()
        em = email.value.strip()
        msg = mensagem.value.strip()

        if not n or not em or not msg:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos."))
            page.snack_bar.open = True
            page.update()
            return

        # validação simples de e-mail
        if not re.match(r"[^@]+@[^@]+\.[^@]+", em):
            page.snack_bar = ft.SnackBar(ft.Text("Email inválido."))
            page.snack_bar.open = True
            page.update()
            return

        # mostra confirmação com os dados enviados (diálogo)
        dlg = ft.AlertDialog(
            title=ft.Text("Formulário enviado"),
            content=ft.Column(
                [
                    ft.Text("O formulário foi enviado com sucesso."),
                    ft.Divider(),
                    ft.Text(f"Nome: {n}"),
                    ft.Text(f"Email: {em}"),
                    ft.Text("Mensagem:"),
                    ft.Text(msg)
                ],
                tight=True
            ),
            actions=[ft.TextButton("Fechar", on_click=fechar_dialog)],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = dlg
        dlg.open = True

        # mostra SnackBar de confirmação imediata
        page.snack_bar = ft.SnackBar(ft.Text("Formulário enviado com sucesso."))
        page.snack_bar.open = True

        # limpa campos do formulário (o diálogo já contém os dados)
        nome.value = ""
        email.value = ""
        mensagem.value = ""

        # mostra confirmação fixa na tela (usa a função adicionada)
        mostrar_confirmacao()

        page.update()

    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar)

    page.add(
        ft.Column(
            [
                ft.Text("Formulário de Contato", size=20),
                nome,
                email,
                mensagem,
                ft.Row([btn_enviar], alignment=ft.MainAxisAlignment.END),
                ft.Divider(),
                status_confirmacao  # exibe confirmação final aqui
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)