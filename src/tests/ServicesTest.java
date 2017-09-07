package tests;

import service.Services;

import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class ServicesTest {
    public static final List<String> expectedListPOIs = Arrays.asList("Lanchonete", "Posto", "Joalheria", "Floricultura", "Pub", "Supermercado", "Churrascaria");
    public static final List<String> expectedNearby = Arrays.asList("Lanchonete", "Joalheria", "Pub", "Supermercado");

    static {    // Setup for testing
        Services.addPOI("Lanchonete", 27, 12);
        Services.addPOI("Posto", 31, 18);
        Services.addPOI("Joalheria", 15, 12);
        Services.addPOI("Floricultura", 19, 21);
        Services.addPOI("Pub", 12, 8);
        Services.addPOI("Supermercado", 23, 6);
        Services.addPOI("Churrascaria", 28, 2);
    }

    @org.junit.Test
    public void listPOIs() throws Exception {
        assertEquals(expectedListPOIs, Services.listPOIs());
    }

    @org.junit.Test
    public void listNearbyPOIs() throws Exception {
        assertEquals(expectedNearby, Services.listNearbyPOIs(20, 10, 10));
    }
}
