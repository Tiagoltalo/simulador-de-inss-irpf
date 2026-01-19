function verificarModalidades() {
    let segurado = document.querySelector("select#segurado").value
    let seguradoModalidades = ["segurado especial", "segurado facultativo", "contribuinte individual", "mei"]
    let modalidades = ["empregado", "empregado doméstico", "trabalhador avulso"]
    let selectModalidadade = document.querySelector("div#div-modalidades")


    if (seguradoModalidades.includes(segurado)) {
        if (segurado === "contribuinte individual") {
            selectModalidadade.innerHTML = `  <label for="modalidades">Modalidades</label>
                                    <select name="modalidade" id="modalidade">
                                        <option value="plano simplificado">Plano Simplificado</option>
                                        <option value="plano normal">Plano Normal</option>
                                        <option value="baixa renda">Baixa Renda</option>
                                    </select>`
        }

        else if (segurado === "segurado facultativo") {
            selectModalidadade.innerHTML = `  <label for="modalidades">Modalidades</label>
                                    <select name="modalidade" id="modalidade">
                                        <option value="baixa renda">Baixa Renda</option>
                                        <option value="plano simplificado">Plano Simplificado</option>
                                        <option value="plano normal">Plano Normal</option>
                                    </select>`
        }

        else if (segurado === "segurado especial") {
            selectModalidadade.innerHTML = `  <label for="modalidades">Modalidades</label>
                                    <select name="modalidade" id="modalidade">
                                        <option value="contribuição obrigatória">Contribuição Obrigatória</option>
                                        <option value="contribuição optativa">Contribuição Optativa</option>
                                    </select>`
        }
    }

    else if (modalidades.includes(segurado)) {
        selectModalidadade.innerHTML = `<label for="modalidades">Modalidades</label>
                                <select name="modalidade" id="modalidade">
                                    <option value="">Selecione</option>
                                </select>`
    }
}