function clicked() {
    var copytext = document.getElementById("copyurl");
    copytext.select();
    copytext.setSelectionRange(0, 99999);
    document.execCommand('copy');
    Swal.fire({
        icon: 'success',
        title: 'Copied',
    })
}

const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#inputPassword');
togglePassword.addEventListener('click', function (e) {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});