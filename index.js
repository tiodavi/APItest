axios.post(URL, postData, config)
  .then((res) => {
    console.log(res.data)
  })
  .catch((error) => {
    console.log(error)
  }) 