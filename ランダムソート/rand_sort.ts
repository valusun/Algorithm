const randomSort = <T>(arr: T[]): T[] => {
  const randint = (min: number, max: number): number => Math.floor((max - min + 1) * Math.random())
  for (let i = arr.length - 1; i > 0; i--) {
    const j = randint(0, i)
    const tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
  }
  return arr
}
