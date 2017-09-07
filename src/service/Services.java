package service;

import model.PointOfInterest;
import storage.Database;
import storage.DummyDB;

import java.util.ArrayList;
import java.util.List;

public final class Services {
    private static final Database db = DummyDB.getInstance();

    private Services() {}

    public static void addPOI(String name, int x, int y) {
        db.addPOI(new PointOfInterest(name, x, y));
    }

    private static List<String> listAsNames(List<PointOfInterest> pois) {
        ArrayList<String> result = new ArrayList<>();

        for (PointOfInterest poi: pois)
            result.add( poi.getName() );

        return result;
    }

    public static List<String> listPOIs() {
        return listAsNames( db.listPOIs() );
    }

    public static List<String> lisNearbytPOIs(int x, int y, int dMax) {
        return listAsNames( db.listNearbyPOIs(x, y, dMax) );
    }

    public static void main(String[] args) {
        addPOI("Lanchonete", 27, 12);
        addPOI("Posto", 31, 18);
        addPOI("Joalheria", 15, 12);
        addPOI("Floricultura", 19, 21);
        addPOI("Pub", 12, 8);
        addPOI("Supermercado", 23, 6);
        addPOI("Churrascaria", 28, 2);

        for (String poi: listPOIs())
            System.out.println(poi);

        System.out.println();

        for (String poi: lisNearbytPOIs(20, 10, 10))
            System.out.println(poi);
    }
}
