utils = {
    axios_post(_url, _body = {}) {
        let headers = {
            "X-CSRFToken": this.data.contactCSRF,
        }
        return axios({
            method: 'POST',
            url: _url,
            data: _body,
            headers: headers
        })
    },
    axios_get(_url) {
        return axios({
            method: 'GET',
            url: _url
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
