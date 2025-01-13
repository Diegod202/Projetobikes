document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('adicionarUsuarioForm');
    const resultadoUsuario = document.getElementById('resultadoUsuario');
    
    let usuarios = [];

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const nome = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const telefone = document.getElementById('telefone').value;

        const novoUsuario = {
            nome: nome,
            email: email,
            telefone: telefone
        };
        usuarios.push(novoUsuario);

        exibirUsuarios();
        
        form.reset();
    });

    function exibirUsuarios() {
        resultadoUsuario.innerHTML = '';

        if (usuarios.length === 0) {
            resultadoUsuario.textContent = 'Nenhum usuário adicionado.';
            return;
        }

        const lista = document.createElement('ul');

        usuarios.forEach((usuario, index) => {
            const item = document.createElement('li');
            item.textContent = `Usuário ${index + 1}: Nome: ${usuario.nome}, Email: ${usuario.email}, Telefone: ${usuario.telefone}`;
            lista.appendChild(item);
        });

        resultadoUsuario.appendChild(lista);
    }

    exibirUsuarios();
});
