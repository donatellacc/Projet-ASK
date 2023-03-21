
const fs = require('fs')
var Document = fs.readFileSync('export_team.csv').toString().split('\r\n')

var SeparatorColumn
var SeparatorValues

var Columns = Document[0]
var Json = []


SeparatorColumn = ','
SeparatorValues = '#'

 Columns = Columns.split(SeparatorColumn)

 for (var i = 0; i < Document.length; i++) {
    var Data = {}
    var Element = Document[i].toString().replace(/\"/g,'').split(SeparatorColumn)
    for (var j = 0; j < Element.length; j++) {
       var Length = (Element[j].split(SeparatorValues)).length
       if (Length > 1) {
         Data[Columns[j]] = Element[j].split(SeparatorValues)
       } else {
         Data[Columns[j]] = Element[j]
       }
    }
    Json.push(Data)
  }

Data = JSON.stringify(Json)

fs.writeFileSync('data1.json', Data, function (err) {
  if (err) throw err
})

//console.log(Json[0])
//console.log(Json[1])
const result = []; //ceci est un Array
Json.map((element_dans_objet) => {
    // ELement c'est ca     // {     //        ID: "Id_du_tag",    //        NameFR:"NomFR_du_tag",    //        NameEN:"NomFR_du_tag",    //        Familles: []    //        parents: [    //            "#Parent1",    //            "#Parent2",    //            ...        ]    //    },     
    result.push({
        id: element_dans_objet["ID"],
        label: element_dans_objet["Name FR"],
        parent: element_dans_objet['Parents']    })
    // fin du tour de boucle 
  })

  result.splice(0,1)

  const result2 = []; //ceci est un Array
  Json.map((element_dans_objet) => {
      // ELement c'est ca     // {     //        ID: "Id_du_tag",    //        NameFR:"NomFR_du_tag",    //        NameEN:"NomFR_du_tag",    //        Familles: []    //        parents: [    //            "#Parent1",    //            "#Parent2",    //            ...        ]    //    },     
      result2.push({
          id: element_dans_objet["Name FR"],
          label: element_dans_objet["Name FR"]   })
      // fin du tour de boucle 
    })
   

Node = JSON.stringify(result2)
  fs.writeFileSync('data-nodes.json', Node, function (err) {
    if (err) throw err
  })
  



var links = [];

result.forEach(function(d){
  if(d.parent){
    links.push({
                target: d.parent[1],
                source: d.label,
                strength: 0.7 });
    }});


//const util = require('util')
//console.log(util.inspect(result, {showHidden: false, depth: null, colors: true}))

Links = JSON.stringify(links)
  fs.writeFileSync('data-links.json', Links, function (err) {
    if (err) throw err
  })


let fichier = fs.readFileSync('data-nodes.json')
let basenodes = JSON.parse(fichier)
console.log(basenodes[1])

let fichier2 = fs.readFileSync('data-links.json')
let baselinks = JSON.parse(fichier2)
console.log(baselinks[1])

const util = require('util')
console.log(util.inspect(basenodes, {showHidden: false, depth: null, colors: true}))
console.log(util.inspect(baselinks, {showHidden: false, depth: null, colors: true}))