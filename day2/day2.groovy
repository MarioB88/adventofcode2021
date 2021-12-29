// PART 1

fname = "day2\\data\\data-day2.txt"
File f = new File(fname)
int hor = 0
int depth = 0

f.eachLine{ l ->
    def line = l.split(" ")
    switch(line[0]){
        case "forward":
            hor+=line[1] as Integer;
            break;
        case "down":
            depth+=line[1] as Integer;
            break;
        case "up":
            depth-=line[1] as Integer;
            break;
    }
}
println(hor*depth)

// PART 2

int aim = 0
hor = 0
depth = 0
f = new File(fname)

f.eachLine{ l ->
    def line = l.split(" ")
    switch(line[0]){
        case "forward":
            hor+=line[1] as Integer;
            depth+=aim*(line[1] as Integer)
            break;
        case "down":
            aim+=line[1] as Integer;
            break;
        case "up":
            aim-=line[1] as Integer;
            break;
    }
}
println(hor*depth)