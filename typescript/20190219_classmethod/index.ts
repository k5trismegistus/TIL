class Klass {
    _name: string

    constructor(name) {
        this._name = name
    }

    static initialize() {
        return new this('kintaro')
    }

    greet() {
        console.log(`hello, ${this._name}`)
    }
}

const k = Klass.initialize()
k.greet()
