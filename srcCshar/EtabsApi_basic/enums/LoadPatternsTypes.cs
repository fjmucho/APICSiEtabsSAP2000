using System;
using System.Collections.Generic;
using System.Text;

namespace EtabsApi
{
    public enum LoadPatternType
    {
        Dead = 1,
        SuperDead = 2,
        Live = 3,
        ReduceLive = 4,
        Quake = 5,
        Wind = 6,
        Snow = 7,
        Other = 8,
        Move = 9,
        Temperature = 10,
        RoofLive = 11,
        Notional = 12,
        PatterLive = 13,
        Wave = 14,
        Braking = 15,
        Centrifugal = 16,
        Friction = 17,
        Ice = 18,
        WindOnLive = 19,
        HorizontalEarthPressure = 20,
        VerticalEarthPressure = 21,
        EarthSurcharge = 22,
        DownDrag = 23,
        VehicleCollision = 24,
        VesselCollision = 25,
        TemperatureGredient = 26,
        Settlement = 27,
        Shrinkage = 28,
        Creep = 29,
        WaterLoadPressure = 30,
        LiveLoadSurcharge = 31,
        LockedInforces = 32,
        PedestrianLL = 33,
        Prestress = 34,
        HyperStatic = 35,
        Buoyancy = 36,
        StreamFlow = 37,
        Impact = 38,
        Construction = 39,
        Seismic=40,
        SeismicDraft=41
    }
}
