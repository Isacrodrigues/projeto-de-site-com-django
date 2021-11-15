(function(win,doc) {
    "use district";
    //verifica se o usuário realmente quer deletar o usuário
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++) {
            btnDel[i].addEventListener('click', function(event){
                if (confirm('Deseja mesmo apagar este usuário?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }



})(window,document);
