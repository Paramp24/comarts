var submit_button = document.querySelector(".btn")
var user_info = document.getElementsByTagName('input')
var data

function post_data_for_login(user_data) {
    try {
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user_data)
        }).then((response)=>{
            return response.json()
        }).then((data)=>{
            if(data){
                location.replace('comarts')
            }else{
                if(location.href.endsWith('/signup')){
                    location.replace('/')
                } else {
                    location.replace('/signup');
                }
            }
            return data
        })
    }
    catch (error) {
        console.error(error)
    }
}

submit_button.addEventListener('click', () => {

    if (user_info[1] == undefined) {
        data = [user_info[0].value]
    } else {
        data = [user_info[0].value, user_info[1].value]
    }
    post_data_for_login(data)
})