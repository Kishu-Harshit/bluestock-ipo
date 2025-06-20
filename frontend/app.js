fetch("http://localhost:3001/api/hello")
  .then(res => res.json())
  .then(data => console.log(data));
