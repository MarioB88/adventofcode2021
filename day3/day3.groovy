// PART 1

fname = "C:\\OwnProjects\\adventofcode2021\\adventofcode2021\\day3\\data\\data-day3.txt"
File f = new File(fname)

List cont1s = []
List cont0s = []

def first_line = f.readLines()[0]
for(i in 0..first_line.length()-1){
    if(first_line[i] == 0){
        cont0s << 0
        cont1s << 0
    }
    else{
        cont0s << 0
        cont1s << 0
    }
}

for(j in 0..first_line.length()-1){
    f.eachLine{l ->
        cont0s[j] = (l.getAt(j) == "0") ? (cont0s.getAt(j)+1) : cont0s.getAt(j)
        cont1s[j] = (l.getAt(j) == "1") ? (cont1s.getAt(j)+1) : cont1s.getAt(j)
    }
}

println(cont0s)
println(cont1s)

i = 0
List gamma = []
List epsilon = []

while(i < cont0s.size){
    gamma << (cont0s.get(i)<=cont1s.get(i))
    i++
}

epsilon = gamma.collect()

Collections.replaceAll(gamma, true, 1)
Collections.replaceAll(gamma, false, 0)
gamma_string = gamma.join()
Collections.replaceAll(epsilon, true, 0)
Collections.replaceAll(epsilon, false, 1)
epsilon_string = epsilon.join()

int gamma_decimal = Integer.parseInt(gamma_string, 2)
int epsilon_decimal = Integer.parseInt(epsilon_string, 2)

println(gamma_decimal)
println(epsilon_decimal)

println(gamma_decimal * epsilon_decimal)


// PART 2

def count_column = {list, index ->
    def counts = [0,0]
    for(l in list){
        if(l[index] == "0"){
            counts[0] += 1
        }else{counts[1] += 1}
    }
    if(counts[0] > counts[1]){return "0"}else{return "1"}
}

List lines_oxygen = f.readLines()
List lines_co2 = f.readLines()
int z = 0

boolean finished = false

int l = 0
for(def k = 0; k<cont0s.size; k++){
    l = 0
    int maximo = count_column.call(lines_oxygen, k)
    while(l < lines_oxygen.size){
        if(lines_oxygen.size < 2){
            finished = true
            break
        }
        if(lines_oxygen.get(l).getAt(k) != maximo){
            lines_oxygen.remove(l)
        }else{l++}
    }
    if(finished){
        break
    }
}

def y = 0
finished = false
for(def k = 0; k<cont0s.size; k++){
    y = 0
    int maximo = count_column.call(lines_co2, k)
    while(y < lines_co2.size){
        if(lines_co2.size < 2){
            finished = true
            break
        }
        if(lines_co2.get(y).getAt(k) == maximo){
            lines_co2.remove(y)
        }else{y++}
    }
    if(finished){
        break
    }
}

co2_string = lines_co2.join()
oxygen_string = lines_oxygen.join()

co2_decimal = Integer.parseInt(co2_string, 2)
oxygen_decimal = Integer.parseInt(oxygen_string, 2)
println(co2_decimal * oxygen_decimal)