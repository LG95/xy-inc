package storage;

import model.PointOfInterest;

import java.util.List;

public interface Database {
    void addPOI(PointOfInterest poi);
    List<PointOfInterest> listPOIs();
    List<PointOfInterest> listNearbyPOIs(int x, int y, int dMax);
}
