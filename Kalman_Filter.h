class SpatialKalman {
  public:
    SpatialKalman() : _x(0), _v(0), _p(1), _q(0.01), _r(0.1) {}
    float filter(float z, float dt) {
      _x += _v * dt; // Predict
      _p += _q;
      float k = _p / (_p + _r); // Update
      float prev_x = _x;
      _x += k * (z - _x);
      _v = (_x - prev_x) / dt;
      _p *= (1 - k);
      return _x;
    }
    float getVelocity() { return _v; }
  private:
    float _x, _v, _p, _q, _r;
};