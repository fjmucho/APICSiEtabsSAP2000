using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
   public class Point: ICloneable 
    {
        public double x { get; set; }
        public double y { get; set; }
        public double z { get; set; }
        public string name { get; set; }
        // analytical results 
        public double u1 { get; set; }
        public double u2 { get; set; }
        public double u3 { get; set; }
        public double r1 { get; set; }
        public double r2 { get; set; }
        public double r3 { get; set; }
        public double f1 { get; set; }
        public double f2 { get; set; }
        public double f3 { get; set; }
        public double m1 { get; set; }
        public double m2 { get; set; }
        public double m3 { get; set; }
        #region Constructors
        public Point(double _x, double _y, double _z, string _name)
        {
            x = _x;
            y = _y;
            z = _z;
            name = _name;
        }
        public Point(double _x, double _y, double _z) : this(_x, _y, _z, "")
        { }
        public Point() : this(0, 0, 0, "")
        { }

        public object Clone()
        {
            return new Point
            {
                x = this.x,
                y = this.y,
                z = this.z,
                name = this.name,
            };
        }


        #endregion
    }
}
