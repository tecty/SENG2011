export function getToken() {
  return localStorage.getItem("token");
}
export function isLogin() {
  // return the bool value of whether there is a token
  return getToken() != null && getToken() != "";
}
