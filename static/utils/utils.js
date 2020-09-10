utils = {
    axios_call(_url, _body = {}, _headers = {}, _method = 'GET') {
        let url = _url
        let method = _method;
        let body = {..._body}
        let headers = {
            "X-CSRFToken": this.data.contactCSRF,
            ..._headers
        }
        return axios({
            method: method,
            url: url,
            data: body,
            headers: headers
        })
    },
    render_star_rating(value) {
        let html = ''
        let star = '<i class="fas fa-star text-warning"></i>'
        let star_empty = '<i class="far fa-star text-warning"></i>'
        let list_stars = [1, 2, 3, 4, 5]
        for (let item in list_stars) {
            if (list_stars[item] <= value) {
                html += star
            } else {
               html += star_empty
            }
        }
        return html
     },
}
