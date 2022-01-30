const sizeData = (num, verbose = false) => {
  const sizeSmall = ['B', 'KB', 'MB', 'GB', 'TB'];
  const sizeBig = ['Bytes','Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes'];
  let size = 0
  while(num > 1000){
    size++
    num/=1000
  }

  return `${num.toFixed(2)} ${verbose ? sizeBig[size] : sizeSmall[size]}`
}

module.exports = {
  sizeData
}