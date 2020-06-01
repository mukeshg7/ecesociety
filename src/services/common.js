import Api from './Api'

export default {
    getMember() {
        return Api().post('api/profile/${id}/')
    },
    getBlogPosts () {
        return Api().get('api/posts/')
      },
}