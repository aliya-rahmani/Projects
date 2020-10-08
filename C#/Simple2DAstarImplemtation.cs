using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace AStar
{
    public class Simple2DAstarImplemtation
    {
        private static AStarMap _Map;
        public static List<AStarNode> GetPath(AStarMap Map)
        {
            _Map = Map;
            List<AStarNode> LocatedPath = new List<AStarNode>();
            bool ValidPath = Search(_Map.SpawnPoint);
            if (ValidPath)
            {
                AStarNode NextNode = _Map.Destination;
                while (NextNode != null)
                {
                    LocatedPath.Add(NextNode);
                    NextNode = NextNode.Parent;
                }
                LocatedPath.Reverse();
            }
            return LocatedPath;
        }
        private static bool Search(AStarNode CurrentNode)
        {
            CurrentNode.State = NodeState.Closed;
            List<AStarNode> NextNodes = GetAdjacentWalkableNodes(CurrentNode);
            NextNodes.Sort((a, b) => a.F.CompareTo(b.F));
            foreach (AStarNode NextNode in NextNodes)
            {
                if (NextNode.Position == _Map.Destination.Position) return true;
                if (Search(NextNode)) return true;
            }
            return false;
        }
        private static List<AStarNode> GetAdjacentWalkableNodes(AStarNode FromNode)
        {
            List<AStarNode> WalkablePoints = new List<AStarNode>();
            List<AStarNode> Locations = GetAdjacentLocations(FromNode);

            foreach (AStarNode NextNode in Locations)
            {
                int X = NextNode.Position.X;
                int Y = NextNode.Position.Y;
                if (X < 0 || X >= _Map.Width || Y < 0 || Y >= _Map.Height) continue;
                if (NextNode.IsSolid) continue;
                if (NextNode.State == NodeState.Closed) continue;

#if DEBUG
                Thread.Sleep(1);
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.SetCursorPosition(NextNode.Position.X, NextNode.Position.Y);
                Console.Write("█");
                Console.ForegroundColor = ConsoleColor.White;
#endif

                if (NextNode.State == NodeState.Open)
                {
                    float TraversalCost = Distance(_Map.Destination.Position, NextNode.Position) + Distance(NextNode.Position, FromNode.Position);
                    float GTemp = FromNode.G + TraversalCost;
                    if (GTemp < NextNode.G)
                    {
                        NextNode.Parent = FromNode;
                        WalkablePoints.Add(NextNode);
                    }
                }
                else
                {
                    NextNode.Parent = FromNode;
                    NextNode.State = NodeState.Open;
                    WalkablePoints.Add(NextNode);
                }
            }
            return WalkablePoints;
        }
        private static float Distance(Point a, Point b)
            => (float)Math.Sqrt(Math.Pow((b.X - a.X), 2) + Math.Pow((b.Y - a.Y), 2));
        private static List<AStarNode> GetAdjacentLocations(AStarNode FromNode)
        {
            List<AStarNode> ReturnValues = new List<AStarNode>();
            int Index = _Map.Nodes.FindIndex((a) => a == FromNode);

            Point[] Around = new Point[] {
                new Point(FromNode.Position.X, FromNode.Position.Y - 1),
                new Point(FromNode.Position.X, FromNode.Position.Y + 1),
                new Point(FromNode.Position.X - 1, FromNode.Position.Y),
                new Point(FromNode.Position.X + 1, FromNode.Position.Y),

                new Point(FromNode.Position.X - 1, FromNode.Position.Y + 1),
                new Point(FromNode.Position.X + 1, FromNode.Position.Y + 1),
                new Point(FromNode.Position.X - 1, FromNode.Position.Y - 1),
                new Point(FromNode.Position.X + 1, FromNode.Position.Y - 1)
            };
            foreach(var z in Around)
            {
                var Point = _Map.Nodes.Find((a) => a.Position == z);
                if (Point != null) ReturnValues.Add(Point);
            }

            return ReturnValues;
        }
    }
    public class AStarMap
    {
        public AStarNode SpawnPoint;
        public AStarNode Destination;
        public int Width;
        public int Height;
        public List<AStarNode> Nodes = new List<AStarNode>();
    }
    public class AStarNode
    {
        public Point Position;
        public bool IsSolid;
        public float G;
        public float H;
        public float F;
        public NodeState State;
        public AStarNode Parent;
    }
    public enum NodeState { Untested, Open, Closed }
}
