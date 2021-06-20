#include "clock.h"

#include <QDateTime>
#include <QTime>

Clock::Clock() {
  const auto now = QDateTime::currentDateTime().time();
  hour_ = now.hour();
  minute_ = now.minute();
  second_ = now.second();

  timer_.start(1000);
  connect(&timer_, &QTimer::timeout, this, &Clock::on_time_out);
}

auto Clock::hour() -> int { return hour_; }

auto Clock::minute() -> int { return minute_; }

auto Clock::second() -> int { return second_; }

void Clock::on_time_out() {
  const auto now = QDateTime::currentDateTime().time();
  hour_ = now.hour();
  emit hourChanged();

  minute_ = now.minute();
  emit minuteChanged();

  second_ = now.second();
  emit secondChanged();
}