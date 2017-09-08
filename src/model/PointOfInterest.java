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

    @Override
    public boolean equals(Object o) {
        if (o instanceof PointOfInterest) {
            PointOfInterest other = (PointOfInterest) o;
            return this.name.equals(other.name) && this.x == other.x && this.y == other.y;
        }

        return false;
    }
}
