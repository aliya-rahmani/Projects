public class SinglyLinkedList<E> {
    private ListNodes<E> head;
    private int size;
    public SinglyLinkedList(){
        this.head = new ListNodes<E>(null);
        this.size = 0;
    }

    public boolean add(int index, E data){
        int counter = 0;
        ListNodes<E> nodeCounter = this.head;
        ListNodes<E> node = new ListNodes<E>(data);
        while (counter <= index){
            nodeCounter = nodeCounter.getNext();
            counter++;
        }
        node.setNext(nodeCounter);
        nodeCounter = this.head;
        while (counter <= index-1){
            nodeCounter = nodeCounter.getNext();
            counter++;
        }
        nodeCounter.setNext(node);
        return true;
    }
}

class ListNodes<E>{
    private ListNodes<E> next = null;
    private E data;
    public ListNodes(E theData){
        this.data = theData;
    }

    public E getData() {
        return data;
    }

    public ListNodes<E> getNext() {
        return next;
    }

    public void setData(E data) {
        this.data = data;
    }

    public void setNext(ListNodes<E> next) {
        this.next = next;
    }
}
