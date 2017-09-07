package storage;

import model.PointOfInterest;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public final class DummyDB implements Database {
    private static final DummyDB instance = new DummyDB();
    private final ArrayList<PointOfInterest> database = new ArrayList<>();

    public static DummyDB getInstance() {
        return instance;
    }

    private DummyDB() {}

    public void addPOI(PointOfInterest poi) {
        this.database.add(poi);
    }

    public List<PointOfInterest> listPOIs() {
        return Collections.unmodifiableList(this.database);
    }

    @Override
    public List<PointOfInterest> listNearbyPOIs(int x, int y, int dMax) {
        ArrayList<PointOfInterest> nearby = new ArrayList<>();
        int dx, dy;

        for (PointOfInterest poi: this.database) {
            dx = poi.getX() - x;
            dy = poi.getY() - y;

            if (Math.sqrt(dx * dx + dy * dy) <= dMax)
                nearby.add(poi);
        }

        return nearby;
    }
}
