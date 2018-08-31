export function authHeader() {
    // return authorization header with jwt token
    // let user = JSON.parse(localStorage.getItem('user'));
    // fetch the token from vuex 
    let token= this.$store.token;

    if (token) {
        // we only need to pass the token backto backend 
        return { 'Authorization': 'JWT ' + token };
    } else {
        return {};
    }
}