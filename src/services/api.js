import axios from 'axios'
import Cookies from 'js-cookie'

const client = axios.create({
  baseURL: 'https://fd966c4b-7372-4de1-b373-fe857aef877d.mock.pstmn.io/api/',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': Cookies.get('csrftoken')
  }
})

export default client