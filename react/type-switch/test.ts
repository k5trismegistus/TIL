interface KlassOne {
  type: 'one'
  onlyKlassOneHasThisValue: string
}

interface KlassTwo {
  type: 'two'
  onlyKlassTwoHasThisValue: string
}

interface Test {
  value: KlassOne | KlassTwo;
}

const f = (t: Test) => {
  switch (t.value.type) {
    case 'one': return t.value.onlyKlassOneHasThisValue
    case 'two': return t.value.onlyKlassTwoHasThisValue
  }
}

console.log(f({
  value: {
    type: 'one',
    onlyKlassOneHasThisValue: 'this is shown',
    // below line raises error
    onlyKlassTwoHasThisValue: 'this is not shown',
  }
}))
// => 'this is shown'