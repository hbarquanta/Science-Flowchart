# Science Flowchart

```mermaid
flowchart TD
    MATH([MATHEMATICS])
    PHYS([PHYSICS])
    CHEM([CHEMISTRY])
    BIO([BIOLOGY])
    ECO([ECOLOGY])
    EARTH([EARTH SCIENCE])
    GEO([GEOLOGY])
    ASTR([ASTRONOMY])

    MATH --> PHYS
    PHYS --> CHEM
    CHEM --> BIO
    BIO --> ECO
    BIO --> EARTH
    EARTH --> GEO
    EARTH --> ASTR
