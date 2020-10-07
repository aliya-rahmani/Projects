//Know that A* is a variation of Dijkstra's Algorithm.
//A* iteratively selects the best route and attempts to see what the next best step is.
/*Helpful Links:
https://www.baeldung.com/java-a-star-pathfinding
https://www.youtube.com/watch?v=ySN5Wnu88nE
*/
import java.util.*;
import java.io.*;
public class AStar{
   public interface GraphNode{ //This represents individual nodes
      String getId(); //Each node has an ID
   }
   public class Graph<T extends GraphNode>{ //This represents the graph
      private final Set<T> nodes;
      private final Map<String, Set<String>> connections;
      
      public T getNode(String id){ //Stores all nodes
         return nodes.stream()
            .filter(node -> node.getId().equals(id))
            .findFirst()
            .orElseThrow(() -> new IllegalArgumentException("No node found with this ID"));
      }
      public Set<T> getConnections(T node){ //Has knowledge of which nodes connect to which
         return connections.get(node.getId()).stream()
         .map(this::getNode)
         .collect(Collectors.toSet());
      }
   }
   public interface Score<T extends GraphNode>{
      double computeCost(T from, T to); //Start and end nodes
   }
   class RouteNode<T extends GraphNode> implements Comparable<RouteNode>{ 
   //Wrappar around nodes that carries extra information. 
   //RouteNode is a computed route instead of the entire graph.
      private final T current;
      private T previous;
      private double routeScore;
      private double estimatedScore;
      
      RouteNode(T current){
         this(current, null, Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY);
      }
      RouteNode(T current, T previous, double routeScore, double estimatedScore){
         this.current = current;
         this.previous = previous;
         this.routeScore = routeScore;
         this.estimatedScore = estimatedScore;
      }
   }
   @Override
   public int compareTo(RouteNode other){ //Orders by estimated score
      if(this.estimatedScore > other.estimatedScore)
         return 1;
      else if(this.estimatedScore<other.estimatedScore)
         return -1; 
      else
         return  0;
   }
   public class RouteFinder<T extends GraphNode>{ //Generates our routes from the graph
      private final Graph<T> graph;
      private final Scorer<T> nextNodeScorer; //Exact score for the next node
      private final Scorer<T> targetScorer; //Estimated score to our destination
      
      public List<T> findRoute(T from, T to){ 
         Queue<T, RouteNode<T>> openSet = new PriorityQueue<>(); //The use of PQ means we will get the best entry off of it
         Map<T, RouteNode<T>> allNodes = new HashMap<>();
         
         RouteNode<T> start = new RouteNode<>(from, null, 0d, targetScorer.computeCost(from, to)); //Open set initially has a single node -- the start point
         openSet.add(start);
         allNodes.put(from, start);
         
         while(!openSet.isEmpty()){ //Iterate until we run out of nodes, or the best available node is our destination
            RouteNode<T> next = openSet.poll();
            if(next.getCurrent().equals(to)){
               List<T> route = new ArrayList<>();
               RouteNode<T> current = next;
               do{
                  route.add(0, current.getCurrent());
                  current = allNodes.get(current.getPrevious());
               } while (current != null);
               return route;    
             }
         }
         //If we havent reached our destination...
         graph.getConnections(next.getCurrent()).forEach(connection -> { 
             RouteNode<T> nextNode = allNodes.getOrDefault(connection, new RouteNode<>(connection));
             allNodes.put(connection, nextNode);
 
             double newScore = next.getRouteScore() + nextNodeScorer.computeCost(next.getCurrent(), connection);
               if (newScore < nextNode.getRouteScore()) {
                 nextNode.setPrevious(next.getCurrent());
                 nextNode.setRouteScore(newScore);
                 nextNode.setEstimatedScore(newScore + targetScorer.computeCost(connection, to));
                 openSet.add(nextNode);
               }
             });
 
             throw new IllegalStateException("No route found :(");  
      }
   
   }
   

}