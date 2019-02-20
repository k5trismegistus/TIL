import * as readlineSync from 'readline-sync'

while (true) {
    let userName = readlineSync.question('あなたの名前は? ')
    console.log(`->こんにちは ${userName}!`)

    let favFood = readlineSync.question('好きな食べ物は? ', {hideEchoBack: true})
    console.log(`->${userName}は${favFood}が好きなんだね!`)
}