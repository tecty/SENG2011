export function getToken() {
  return localStorage.getItem("token");
}
export function getUsername() {
  return localStorage.getItem("username");
}
export function isLogin() {
  // return the bool value of whether there is a token
  return getToken() != null && getToken() != "";
}