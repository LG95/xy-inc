package tests;

import model.PointOfInterest;
import storage.Database;
import storage.DummyDB;

import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class DatabaseTest {
    private static final PointOfInterest lanchonete = new PointOfInterest("Lanchonete", 27, 12);
    private static final PointOfInterest posto = new PointOfInterest("Posto", 31, 18);
    private static final PointOfInterest joalheria = new PointOfInterest("Joalheria", 15, 12);
    private static final PointOfInterest floricultura = new PointOfInterest("Floricultura", 19, 21);
    private static final PointOfInterest pub = new PointOfInterest("Pub", 12, 8);
    private static final PointOfInterest supermercado = new PointOfInterest("Supermercado", 23, 6);
    private static final PointOfInterest churrascaria = new PointOfInterest("Churrascaria", 28, 2);
    private static final List<PointOfInterest> expectedNearby = Arrays.asList(lanchonete, joalheria, pub, supermercado);
    private static final List<PointOfInterest> expectedListPOIs = Arrays.asList(lanchonete, posto, joalheria, floricultura, pub, supermercado, churrascaria);
    private static final Database db = DummyDB.getInstance();

    static {    // Setup for testing
        db.addPOI(lanchonete);
        db.addPOI(posto);
        db.addPOI(joalheria);
        db.addPOI(floricultura);
        db.addPOI(pub);
        db.addPOI(supermercado);
        db.addPOI(churrascaria);
    }

    @org.junit.Test
    public void listPOIs() throws Exception {
        assertEquals(expectedListPOIs, db.listPOIs());
    }

    @org.junit.Test
    public void listNearbyPOIs() throws Exception {
        assertEquals(expectedNearby, db.listNearbyPOIs(20, 10, 10));
    }

}
