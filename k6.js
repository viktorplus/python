import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
//   vus: 10, // virtual users
//   duration: '20s',
//   iterations: 1000
   stages: [
       { duration: '1m', target: '100'},
       { duration: '1h', target: '100'},
       { duration: '1m', target: '0'}
    //    { duration: '30s', target: '0'},
   ]
};

export default function () {
  let res = http.get('https://test.k6.io');
  check(res, { 'status was 200': (r) => r.status === 200 });
  sleep(1);
}