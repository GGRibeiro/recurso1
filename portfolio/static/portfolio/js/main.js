
class MobileNavbar {
  constructor(mobileMenu, navList, navLinks) {
    this.mobileMenu = document.querySelector(mobileMenu);
    this.navList = document.querySelector(navList);
    this.navLinks = document.querySelectorAll(navLinks);
    this.activeClass = "active";

    this.ClickRato = this.ClickRato.bind(this);
    // o metodo bind retorna uma nova funcao que quando eu invoco tem o this configurado para o que eu quiser
    //o bind faz o this se referir a classe
  }

  ClickRato() {
    //erro de undefined no botao, this perde a referencia
    //console.log();
    this.navList.classList.toggle(this.activeClass);
    this.mobileMenu.classList.toggle(this.activeClass);

  }

  addEvento() {
    this.mobileMenu.addEventListener("click", this.ClickRato);
  }

  init() {
    if (this.mobileMenu) { /* o metodo vai inicair a funcao se mobileMenu existe no documento  */
      this.addEvento();
    }
    return this;
  }
}

const mobileNavbar = new MobileNavbar(
  ".mobileMenu",
  ".navList",
  ".navList li",
);
mobileNavbar.init();


/*----------------------------------------- */
const darkModeBtn = document.getElementById('darkBtn');
const body = document.querySelector('body'); //o body é a a parte do html que irá afetar

darkModeBtn.addEventListener('click', () => {
  body.classList.toggle('darkMode');
});
//--------------------------------------------------///


//-------data------///
const d = new Date();
document.getElementById("demo").innerHTML = d;
//-----------///////


//**        ---nome---
function exibeNome() {
  var nome = document.getElementById("nome").value;
  document.getElementById("resultado").innerHTML = "Olá " + nome + "!";
}




//**        ---nome---   */

function exibeTexto() {
  var texto = document.getElementById("texto").value;
  document.getElementById("textoEscrito").innerHTML = " " + texto + " ";
}





