import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START
    tarefas_view = ft.ListView(expand=True, spacing=8, padding=10)
    entrada = ft.TextField(hint_text="Digite o nome da tarefa", expand=True)

    # Dropdown para prioridade
    prioridade_dropdown = ft.Dropdown(
        width=120,
        options=[
            ft.dropdown.Option("Alta"),
            ft.dropdown.Option("Média"),
            ft.dropdown.Option("Baixa"),
        ],
        value="Média"
    )

    def remover_tarefa(e, tarefa_item):
        if tarefa_item in tarefas_view.controls:
            tarefas_view.controls.remove(tarefa_item)
            page.update()

    def adicionar_tarefa(e=None):
        texto = entrada.value.strip()
        if not texto:
            page.snack_bar = ft.SnackBar(ft.Text("Digite uma tarefa válida."))
            page.snack_bar.open = True
            page.update()
            return

        # metadados: timestamp e rank de prioridade
        prioridade = prioridade_dropdown.value or "Média"
        rank_map = {"Alta": 1, "Média": 2, "Baixa": 3}
        ts = datetime.datetime.now().timestamp()

        delete_button = ft.TextButton("Remover")
        checkbox = ft.Checkbox(label=texto, expand=True)
        tarefa_item = ft.Row(
            [
                checkbox,
                ft.Text(f"({prioridade})"),
                delete_button
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        # anexar metadados diretamente no objeto
        tarefa_item._meta = {"created_ts": ts, "priority": prioridade, "priority_rank": rank_map.get(prioridade, 99)}

        delete_button.on_click = lambda ev, it=tarefa_item: remover_tarefa(ev, it)

        tarefas_view.controls.append(tarefa_item)
        entrada.value = ""
        page.update()

    # permitir adicionar também ao pressionar Enter
    entrada.on_submit = adicionar_tarefa

    # --- novas opções de ordenação ---
    def ordenar_por_data(e):
        tarefas_view.controls.sort(key=lambda row: getattr(row, "_meta", {}).get("created_ts", 0))
        page.update()

    def ordenar_por_prioridade(e):
        tarefas_view.controls.sort(key=lambda row: getattr(row, "_meta", {}).get("priority_rank", 99))
        page.update()

    def remover_ultima(e):
        if tarefas_view.controls:
            remover_tarefa(e, tarefas_view.controls[-1])
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Nenhuma tarefa para remover."))
            page.snack_bar.open = True
            page.update()

    def close_dialog(e):
        if page.dialog:
            page.dialog.open = False
            page.update()

    def limpar_todas(e):
        if not tarefas_view.controls:
            page.snack_bar = ft.SnackBar(ft.Text("Lista já está vazia."))
            page.snack_bar.open = True
            page.update()
            return
        tarefas_view.controls.clear()
        page.update()

    # botões extras (mostrar_tarefas removido)
    btn_remover_ultima = ft.ElevatedButton("Remover última", on_click=remover_ultima)
    btn_sort_date = ft.ElevatedButton("Ordenar por data", on_click=ordenar_por_data)
    btn_sort_priority = ft.ElevatedButton("Ordenar por prioridade", on_click=ordenar_por_prioridade)
    btn_limpar = ft.TextButton("Limpar tudo", on_click=limpar_todas)

    # barra com campo, prioridade e botões
    barra = ft.Row(
        [
            entrada,
            prioridade_dropdown,
            ft.Row(
                [
                    ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa),
                    btn_remover_ultima,
                    btn_sort_date,
                    btn_sort_priority,
                    btn_limpar
                ],
                spacing=8
            )
        ],
        spacing=8
    )

    page.add(
        ft.Column(
            [
                ft.Text("Minha Lista de Tarefas", size=20),
                barra,
                tarefas_view
            ],
            expand=True
        )
    )

    # popula a lista com algumas tarefas iniciais (usa adicionar_tarefa para reutilizar lógica)
    tarefas_iniciais = [("Comprar leite", "Média"), ("Estudar Python", "Alta"), ("Enviar relatório", "Baixa")]
    for t, p in tarefas_iniciais:
        entrada.value = t
        prioridade_dropdown.value = p
        adicionar_tarefa()

if __name__ == "__main__":
    ft.app(target=main)