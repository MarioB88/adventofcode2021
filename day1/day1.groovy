def fname = "day1\\data\\data-day1.txt"
File f = new File(fname)
List numbers = f.text.split("\n")
def prevn = numbers[0]
int contador = 0

numbers.each{
    if(prevn < it){
        contador++
    }
    prevn = it
}
println(contador)

// Part 1 hecha
contador2 = 0
def contar_slices = {
    for(def i=0; i<=(numbers.size - 4); i++){
        sum3 = numbers[i..i+2].sum()
        sum4 = numbers[i+1..i+3].sum()
        contador2 = (sum3<sum4) ? (contador2+1) : contador2
    }
    return contador2
}

def result = contar_slices.call()
println(result)