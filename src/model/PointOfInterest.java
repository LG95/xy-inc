package model;

public final class PointOfInterest {
    private final String name;
    private final int x;
    private final int y;

    public PointOfInterest(String name, int x, int y) {
        this.name = name;
        this.x = x;
        this.y = y;
    }

    public String getName() {
        return name;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
