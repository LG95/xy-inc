package service;

import model.PointOfInterest;
import storage.Database;
import storage.SQLiteDB;

import java.util.ArrayList;
import java.util.List;

public final class Services {
    private static final Database db = SQLiteDB.getInstance();

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

    public static List<String> listNearbyPOIs(int x, int y, int dMax) {
        return listAsNames( db.listNearbyPOIs(x, y, dMax) );
    }

    public static void main(String[] args) {}
}
