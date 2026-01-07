Hyperdrift is a panelized LED matrix artwork.

![](attachments/Hyperdrift-rendering.png)


# LED panels
Each panel can have an arbitrary layout of LEDs, as long as they are electrically connected in a 4x16 matrix (4 common cathodes, 16 anodes).

## Mechanical specification

- [Spec PDF](https://github.com/combs/Hyperdrift/raw/refs/heads/main/Mechanical%20specs/Hyperdrift-Mechanical%20spec%20for%20LED%20panels.pdf) 


## Example LED panel layouts

### Grid
This is a straightforward grid of 8x8 pixels.
- [KiCad board and schematic](https://github.com/combs/Hyperdrift/tree/main/LED%20panel%20reference%20design%20-%20Grid)
- [BOM](https://github.com/combs/Hyperdrift/raw/refs/heads/main/LED%20panel%20reference%20design%20-%20Grid/bom/ibom.html) (download and open)
- [Schematic PDF](https://github.com/combs/Hyperdrift/raw/refs/heads/main/LED%20panel%20reference%20design%20-%20Grid/Hyperdrift-Grid.pdf) 
- [Board PDF](https://github.com/combs/Hyperdrift/raw/refs/heads/main/LED%20panel%20reference%20design%20-%20Grid/plots/Hyperdrift-Grid__Assembly.pdf) 


# Display controllers

Each display controller is a 75x100mm board that drives three LED panels (12x16 matrix arrangement). It accepts 12V in. It is designed to allow for either daisy-chained or wagon-wheel bus arrangement.

- [KiCad board and schematic](https://github.com/combs/Hyperdrift/tree/main/Display%20controller)
- [BOM](https://github.com/combs/Hyperdrift/raw/refs/heads/main/Display%20controller/bom/ibom.html) (download and open)
- [Schematic PDF](https://github.com/combs/Hyperdrift/raw/refs/heads/main/Display%20controller/Hyperdrift-Display-Controller.pdf) 
- [Board PDF](https://github.com/combs/Hyperdrift/raw/refs/heads/main/Display%20controller/Hyperdrift-Display-Controller-board.pdf) 