package main

import (
	"fmt"
	"sync"
	"time"
)

//ChopS struct
type ChopS struct{ sync.Mutex }

//Philo struct
type Philo struct {
	leftCS, rightCS *ChopS
	number          int
}

var on sync.Once

func setup() {
	fmt.Println("Init philosopher")
}

func host(ch chan int) {
	ch <- 1
	ch <- 2
	<-ch
}

func (p Philo) eat(ch chan int) {

	on.Do(setup)

	for i := 0; i < 3; i++ {

		<-ch

		fmt.Printf("starting to eat %d\n", p.number)

		p.leftCS.Lock()
		p.rightCS.Lock()

		fmt.Printf("finishing eating %d\n", p.number)

		p.rightCS.Unlock()
		p.leftCS.Unlock()

		ch <- i
	}
	return
}

func main() {
	ch := make(chan int, 2)

	//c := make(chan int)

	CSticks := make([]*ChopS, 5)
	for i := 0; i < 5; i++ {
		CSticks[i] = new(ChopS)
	}

	philos := make([]*Philo, 5)
	for i := 0; i < 5; i++ {
		philos[i] = &Philo{CSticks[i], CSticks[(i+1)%5], i + 1}
	}

	go host(ch)

	for i := 0; i < 5; i++ {
		go philos[i].eat(ch)
	}

	time.Sleep(1000 * time.Millisecond)
}