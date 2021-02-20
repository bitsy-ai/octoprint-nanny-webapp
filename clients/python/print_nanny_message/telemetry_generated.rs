// automatically generated by the FlatBuffers compiler, do not modify



use std::mem;
use std::cmp::Ordering;

extern crate flatbuffers;
use self::flatbuffers::EndianScalar;

#[allow(unused_imports, dead_code)]
pub mod print_nanny_message {

  use std::mem;
  use std::cmp::Ordering;

  extern crate flatbuffers;
  use self::flatbuffers::EndianScalar;
#[allow(unused_imports, dead_code)]
pub mod telemetry {

  use std::mem;
  use std::cmp::Ordering;

  extern crate flatbuffers;
  use self::flatbuffers::EndianScalar;

#[allow(non_camel_case_types)]
#[repr(i8)]
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
pub enum PluginEvent {
  bounding_box_predict = 0,
  monitoring_frame_raw = 1,
  monitoring_frame_post = 2,
  device_register_start = 3,
  device_register_done = 4,
  device_register_failed = 5,
  printer_profile_sync_start = 6,
  printer_profile_sync_done = 7,
  printer_profile_sync_failed = 9,

}

pub const ENUM_MIN_PLUGIN_EVENT: i8 = 0;
pub const ENUM_MAX_PLUGIN_EVENT: i8 = 9;

impl<'a> flatbuffers::Follow<'a> for PluginEvent {
  type Inner = Self;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    flatbuffers::read_scalar_at::<Self>(buf, loc)
  }
}

impl flatbuffers::EndianScalar for PluginEvent {
  #[inline]
  fn to_little_endian(self) -> Self {
    let n = i8::to_le(self as i8);
    let p = &n as *const i8 as *const PluginEvent;
    unsafe { *p }
  }
  #[inline]
  fn from_little_endian(self) -> Self {
    let n = i8::from_le(self as i8);
    let p = &n as *const i8 as *const PluginEvent;
    unsafe { *p }
  }
}

impl flatbuffers::Push for PluginEvent {
    type Output = PluginEvent;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        flatbuffers::emplace_scalar::<PluginEvent>(dst, *self);
    }
}

#[allow(non_camel_case_types)]
pub const ENUM_VALUES_PLUGIN_EVENT:[PluginEvent; 9] = [
  PluginEvent::bounding_box_predict,
  PluginEvent::monitoring_frame_raw,
  PluginEvent::monitoring_frame_post,
  PluginEvent::device_register_start,
  PluginEvent::device_register_done,
  PluginEvent::device_register_failed,
  PluginEvent::printer_profile_sync_start,
  PluginEvent::printer_profile_sync_done,
  PluginEvent::printer_profile_sync_failed
];

#[allow(non_camel_case_types)]
pub const ENUM_NAMES_PLUGIN_EVENT:[&'static str; 10] = [
    "bounding_box_predict",
    "monitoring_frame_raw",
    "monitoring_frame_post",
    "device_register_start",
    "device_register_done",
    "device_register_failed",
    "printer_profile_sync_start",
    "printer_profile_sync_done",
    "",
    "printer_profile_sync_failed"
];

pub fn enum_name_plugin_event(e: PluginEvent) -> &'static str {
  let index = e as i8;
  ENUM_NAMES_PLUGIN_EVENT[index as usize]
}

#[allow(non_camel_case_types)]
#[repr(i8)]
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
pub enum RemoteCommand {
  print_start = 0,
  print_stop = 1,
  print_pause = 2,
  print_resume = 3,
  snapshot = 4,
  moze_nozzle = 5,
  monitoring_start = 6,
  monitoring_stop = 7,

}

pub const ENUM_MIN_REMOTE_COMMAND: i8 = 0;
pub const ENUM_MAX_REMOTE_COMMAND: i8 = 7;

impl<'a> flatbuffers::Follow<'a> for RemoteCommand {
  type Inner = Self;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    flatbuffers::read_scalar_at::<Self>(buf, loc)
  }
}

impl flatbuffers::EndianScalar for RemoteCommand {
  #[inline]
  fn to_little_endian(self) -> Self {
    let n = i8::to_le(self as i8);
    let p = &n as *const i8 as *const RemoteCommand;
    unsafe { *p }
  }
  #[inline]
  fn from_little_endian(self) -> Self {
    let n = i8::from_le(self as i8);
    let p = &n as *const i8 as *const RemoteCommand;
    unsafe { *p }
  }
}

impl flatbuffers::Push for RemoteCommand {
    type Output = RemoteCommand;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        flatbuffers::emplace_scalar::<RemoteCommand>(dst, *self);
    }
}

#[allow(non_camel_case_types)]
pub const ENUM_VALUES_REMOTE_COMMAND:[RemoteCommand; 8] = [
  RemoteCommand::print_start,
  RemoteCommand::print_stop,
  RemoteCommand::print_pause,
  RemoteCommand::print_resume,
  RemoteCommand::snapshot,
  RemoteCommand::moze_nozzle,
  RemoteCommand::monitoring_start,
  RemoteCommand::monitoring_stop
];

#[allow(non_camel_case_types)]
pub const ENUM_NAMES_REMOTE_COMMAND:[&'static str; 8] = [
    "print_start",
    "print_stop",
    "print_pause",
    "print_resume",
    "snapshot",
    "moze_nozzle",
    "monitoring_start",
    "monitoring_stop"
];

pub fn enum_name_remote_command(e: RemoteCommand) -> &'static str {
  let index = e as i8;
  ENUM_NAMES_REMOTE_COMMAND[index as usize]
}

#[allow(non_camel_case_types)]
#[repr(u8)]
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
pub enum MessageType {
  NONE = 0,
  MonitoringFrameRaw = 1,
  MonitoringFramePost = 2,
  BoundingBoxes = 3,

}

pub const ENUM_MIN_MESSAGE_TYPE: u8 = 0;
pub const ENUM_MAX_MESSAGE_TYPE: u8 = 3;

impl<'a> flatbuffers::Follow<'a> for MessageType {
  type Inner = Self;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    flatbuffers::read_scalar_at::<Self>(buf, loc)
  }
}

impl flatbuffers::EndianScalar for MessageType {
  #[inline]
  fn to_little_endian(self) -> Self {
    let n = u8::to_le(self as u8);
    let p = &n as *const u8 as *const MessageType;
    unsafe { *p }
  }
  #[inline]
  fn from_little_endian(self) -> Self {
    let n = u8::from_le(self as u8);
    let p = &n as *const u8 as *const MessageType;
    unsafe { *p }
  }
}

impl flatbuffers::Push for MessageType {
    type Output = MessageType;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        flatbuffers::emplace_scalar::<MessageType>(dst, *self);
    }
}

#[allow(non_camel_case_types)]
pub const ENUM_VALUES_MESSAGE_TYPE:[MessageType; 4] = [
  MessageType::NONE,
  MessageType::MonitoringFrameRaw,
  MessageType::MonitoringFramePost,
  MessageType::BoundingBoxes
];

#[allow(non_camel_case_types)]
pub const ENUM_NAMES_MESSAGE_TYPE:[&'static str; 4] = [
    "NONE",
    "MonitoringFrameRaw",
    "MonitoringFramePost",
    "BoundingBoxes"
];

pub fn enum_name_message_type(e: MessageType) -> &'static str {
  let index = e as u8;
  ENUM_NAMES_MESSAGE_TYPE[index as usize]
}

pub struct MessageTypeUnionTableOffset {}
// struct Box, aligned to 4
#[repr(C, align(4))]
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Box {
  ymin_: f32,
  ymax_: f32,
  xmin_: f32,
  xmax_: f32,
  score_: f32,
  class_index_: i8,
  padding0__: u8,  padding1__: u16,
} // pub struct Box
impl flatbuffers::SafeSliceAccess for Box {}
impl<'a> flatbuffers::Follow<'a> for Box {
  type Inner = &'a Box;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    <&'a Box>::follow(buf, loc)
  }
}
impl<'a> flatbuffers::Follow<'a> for &'a Box {
  type Inner = &'a Box;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    flatbuffers::follow_cast_ref::<Box>(buf, loc)
  }
}
impl<'b> flatbuffers::Push for Box {
    type Output = Box;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        let src = unsafe {
            ::std::slice::from_raw_parts(self as *const Box as *const u8, Self::size())
        };
        dst.copy_from_slice(src);
    }
}
impl<'b> flatbuffers::Push for &'b Box {
    type Output = Box;

    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        let src = unsafe {
            ::std::slice::from_raw_parts(*self as *const Box as *const u8, Self::size())
        };
        dst.copy_from_slice(src);
    }
}


impl Box {
  pub fn new<'a>(_ymin: f32, _ymax: f32, _xmin: f32, _xmax: f32, _score: f32, _class_index: i8) -> Self {
    Box {
      ymin_: _ymin.to_little_endian(),
      ymax_: _ymax.to_little_endian(),
      xmin_: _xmin.to_little_endian(),
      xmax_: _xmax.to_little_endian(),
      score_: _score.to_little_endian(),
      class_index_: _class_index.to_little_endian(),

      padding0__: 0,padding1__: 0,
    }
  }
  pub fn ymin<'a>(&'a self) -> f32 {
    self.ymin_.from_little_endian()
  }
  pub fn ymax<'a>(&'a self) -> f32 {
    self.ymax_.from_little_endian()
  }
  pub fn xmin<'a>(&'a self) -> f32 {
    self.xmin_.from_little_endian()
  }
  pub fn xmax<'a>(&'a self) -> f32 {
    self.xmax_.from_little_endian()
  }
  pub fn score<'a>(&'a self) -> f32 {
    self.score_.from_little_endian()
  }
  pub fn class_index<'a>(&'a self) -> i8 {
    self.class_index_.from_little_endian()
  }
}

pub enum ImageOffset {}
#[derive(Copy, Clone, Debug, PartialEq)]

pub struct Image<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Image<'a> {
    type Inner = Image<'a>;
    #[inline]
    fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
        Self {
            _tab: flatbuffers::Table { buf: buf, loc: loc },
        }
    }
}

impl<'a> Image<'a> {
    #[inline]
    pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
        Image {
            _tab: table,
        }
    }
    #[allow(unused_mut)]
    pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
        _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
        args: &'args ImageArgs<'args>) -> flatbuffers::WIPOffset<Image<'bldr>> {
      let mut builder = ImageBuilder::new(_fbb);
      if let Some(x) = args.data { builder.add_data(x); }
      builder.add_height(args.height);
      builder.add_width(args.width);
      builder.finish()
    }

    pub const VT_WIDTH: flatbuffers::VOffsetT = 4;
    pub const VT_HEIGHT: flatbuffers::VOffsetT = 6;
    pub const VT_DATA: flatbuffers::VOffsetT = 8;

  #[inline]
  pub fn width(&self) -> i16 {
    self._tab.get::<i16>(Image::VT_WIDTH, Some(0)).unwrap()
  }
  #[inline]
  pub fn height(&self) -> i16 {
    self._tab.get::<i16>(Image::VT_HEIGHT, Some(0)).unwrap()
  }
  #[inline]
  pub fn data(&self) -> Option<&'a [i8]> {
    self._tab.get::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<'a, i8>>>(Image::VT_DATA, None).map(|v| v.safe_slice())
  }
}

pub struct ImageArgs<'a> {
    pub width: i16,
    pub height: i16,
    pub data: Option<flatbuffers::WIPOffset<flatbuffers::Vector<'a ,  i8>>>,
}
impl<'a> Default for ImageArgs<'a> {
    #[inline]
    fn default() -> Self {
        ImageArgs {
            width: 0,
            height: 0,
            data: None,
        }
    }
}
pub struct ImageBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> ImageBuilder<'a, 'b> {
  #[inline]
  pub fn add_width(&mut self, width: i16) {
    self.fbb_.push_slot::<i16>(Image::VT_WIDTH, width, 0);
  }
  #[inline]
  pub fn add_height(&mut self, height: i16) {
    self.fbb_.push_slot::<i16>(Image::VT_HEIGHT, height, 0);
  }
  #[inline]
  pub fn add_data(&mut self, data: flatbuffers::WIPOffset<flatbuffers::Vector<'b , i8>>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(Image::VT_DATA, data);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> ImageBuilder<'a, 'b> {
    let start = _fbb.start_table();
    ImageBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Image<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

pub enum MonitoringFrameRawOffset {}
#[derive(Copy, Clone, Debug, PartialEq)]

pub struct MonitoringFrameRaw<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for MonitoringFrameRaw<'a> {
    type Inner = MonitoringFrameRaw<'a>;
    #[inline]
    fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
        Self {
            _tab: flatbuffers::Table { buf: buf, loc: loc },
        }
    }
}

impl<'a> MonitoringFrameRaw<'a> {
    #[inline]
    pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
        MonitoringFrameRaw {
            _tab: table,
        }
    }
    #[allow(unused_mut)]
    pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
        _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
        args: &'args MonitoringFrameRawArgs<'args>) -> flatbuffers::WIPOffset<MonitoringFrameRaw<'bldr>> {
      let mut builder = MonitoringFrameRawBuilder::new(_fbb);
      if let Some(x) = args.image { builder.add_image(x); }
      builder.add_ts(args.ts);
      builder.add_event_type(args.event_type);
      builder.finish()
    }

    pub const VT_TS: flatbuffers::VOffsetT = 4;
    pub const VT_IMAGE: flatbuffers::VOffsetT = 6;
    pub const VT_EVENT_TYPE: flatbuffers::VOffsetT = 8;

  #[inline]
  pub fn ts(&self) -> u32 {
    self._tab.get::<u32>(MonitoringFrameRaw::VT_TS, Some(0)).unwrap()
  }
  #[inline]
  pub fn image(&self) -> Option<Image<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<Image<'a>>>(MonitoringFrameRaw::VT_IMAGE, None)
  }
  #[inline]
  pub fn event_type(&self) -> PluginEvent {
    self._tab.get::<PluginEvent>(MonitoringFrameRaw::VT_EVENT_TYPE, Some(PluginEvent::monitoring_frame_raw)).unwrap()
  }
}

pub struct MonitoringFrameRawArgs<'a> {
    pub ts: u32,
    pub image: Option<flatbuffers::WIPOffset<Image<'a >>>,
    pub event_type: PluginEvent,
}
impl<'a> Default for MonitoringFrameRawArgs<'a> {
    #[inline]
    fn default() -> Self {
        MonitoringFrameRawArgs {
            ts: 0,
            image: None,
            event_type: PluginEvent::monitoring_frame_raw,
        }
    }
}
pub struct MonitoringFrameRawBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> MonitoringFrameRawBuilder<'a, 'b> {
  #[inline]
  pub fn add_ts(&mut self, ts: u32) {
    self.fbb_.push_slot::<u32>(MonitoringFrameRaw::VT_TS, ts, 0);
  }
  #[inline]
  pub fn add_image(&mut self, image: flatbuffers::WIPOffset<Image<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<Image>>(MonitoringFrameRaw::VT_IMAGE, image);
  }
  #[inline]
  pub fn add_event_type(&mut self, event_type: PluginEvent) {
    self.fbb_.push_slot::<PluginEvent>(MonitoringFrameRaw::VT_EVENT_TYPE, event_type, PluginEvent::monitoring_frame_raw);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> MonitoringFrameRawBuilder<'a, 'b> {
    let start = _fbb.start_table();
    MonitoringFrameRawBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<MonitoringFrameRaw<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

pub enum MonitoringFramePostOffset {}
#[derive(Copy, Clone, Debug, PartialEq)]

pub struct MonitoringFramePost<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for MonitoringFramePost<'a> {
    type Inner = MonitoringFramePost<'a>;
    #[inline]
    fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
        Self {
            _tab: flatbuffers::Table { buf: buf, loc: loc },
        }
    }
}

impl<'a> MonitoringFramePost<'a> {
    #[inline]
    pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
        MonitoringFramePost {
            _tab: table,
        }
    }
    #[allow(unused_mut)]
    pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
        _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
        args: &'args MonitoringFramePostArgs<'args>) -> flatbuffers::WIPOffset<MonitoringFramePost<'bldr>> {
      let mut builder = MonitoringFramePostBuilder::new(_fbb);
      if let Some(x) = args.raw { builder.add_raw(x); }
      if let Some(x) = args.image { builder.add_image(x); }
      builder.add_ts(args.ts);
      builder.add_event_type(args.event_type);
      builder.finish()
    }

    pub const VT_TS: flatbuffers::VOffsetT = 4;
    pub const VT_IMAGE: flatbuffers::VOffsetT = 6;
    pub const VT_RAW: flatbuffers::VOffsetT = 8;
    pub const VT_EVENT_TYPE: flatbuffers::VOffsetT = 10;

  #[inline]
  pub fn ts(&self) -> u32 {
    self._tab.get::<u32>(MonitoringFramePost::VT_TS, Some(0)).unwrap()
  }
  #[inline]
  pub fn image(&self) -> Option<Image<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<Image<'a>>>(MonitoringFramePost::VT_IMAGE, None)
  }
  #[inline]
  pub fn raw(&self) -> Option<MonitoringFrameRaw<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<MonitoringFrameRaw<'a>>>(MonitoringFramePost::VT_RAW, None)
  }
  #[inline]
  pub fn event_type(&self) -> PluginEvent {
    self._tab.get::<PluginEvent>(MonitoringFramePost::VT_EVENT_TYPE, Some(PluginEvent::monitoring_frame_post)).unwrap()
  }
}

pub struct MonitoringFramePostArgs<'a> {
    pub ts: u32,
    pub image: Option<flatbuffers::WIPOffset<Image<'a >>>,
    pub raw: Option<flatbuffers::WIPOffset<MonitoringFrameRaw<'a >>>,
    pub event_type: PluginEvent,
}
impl<'a> Default for MonitoringFramePostArgs<'a> {
    #[inline]
    fn default() -> Self {
        MonitoringFramePostArgs {
            ts: 0,
            image: None,
            raw: None,
            event_type: PluginEvent::monitoring_frame_post,
        }
    }
}
pub struct MonitoringFramePostBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> MonitoringFramePostBuilder<'a, 'b> {
  #[inline]
  pub fn add_ts(&mut self, ts: u32) {
    self.fbb_.push_slot::<u32>(MonitoringFramePost::VT_TS, ts, 0);
  }
  #[inline]
  pub fn add_image(&mut self, image: flatbuffers::WIPOffset<Image<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<Image>>(MonitoringFramePost::VT_IMAGE, image);
  }
  #[inline]
  pub fn add_raw(&mut self, raw: flatbuffers::WIPOffset<MonitoringFrameRaw<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<MonitoringFrameRaw>>(MonitoringFramePost::VT_RAW, raw);
  }
  #[inline]
  pub fn add_event_type(&mut self, event_type: PluginEvent) {
    self.fbb_.push_slot::<PluginEvent>(MonitoringFramePost::VT_EVENT_TYPE, event_type, PluginEvent::monitoring_frame_post);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> MonitoringFramePostBuilder<'a, 'b> {
    let start = _fbb.start_table();
    MonitoringFramePostBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<MonitoringFramePost<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

pub enum BoundingBoxesOffset {}
#[derive(Copy, Clone, Debug, PartialEq)]

pub struct BoundingBoxes<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for BoundingBoxes<'a> {
    type Inner = BoundingBoxes<'a>;
    #[inline]
    fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
        Self {
            _tab: flatbuffers::Table { buf: buf, loc: loc },
        }
    }
}

impl<'a> BoundingBoxes<'a> {
    #[inline]
    pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
        BoundingBoxes {
            _tab: table,
        }
    }
    #[allow(unused_mut)]
    pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
        _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
        args: &'args BoundingBoxesArgs<'args>) -> flatbuffers::WIPOffset<BoundingBoxes<'bldr>> {
      let mut builder = BoundingBoxesBuilder::new(_fbb);
      if let Some(x) = args.boxes { builder.add_boxes(x); }
      if let Some(x) = args.post_image { builder.add_post_image(x); }
      if let Some(x) = args.original_image { builder.add_original_image(x); }
      builder.add_ts(args.ts);
      builder.add_event_type(args.event_type);
      builder.finish()
    }

    pub const VT_TS: flatbuffers::VOffsetT = 4;
    pub const VT_ORIGINAL_IMAGE: flatbuffers::VOffsetT = 6;
    pub const VT_POST_IMAGE: flatbuffers::VOffsetT = 8;
    pub const VT_BOXES: flatbuffers::VOffsetT = 10;
    pub const VT_EVENT_TYPE: flatbuffers::VOffsetT = 12;

  #[inline]
  pub fn ts(&self) -> u32 {
    self._tab.get::<u32>(BoundingBoxes::VT_TS, Some(0)).unwrap()
  }
  #[inline]
  pub fn original_image(&self) -> Option<Image<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<Image<'a>>>(BoundingBoxes::VT_ORIGINAL_IMAGE, None)
  }
  #[inline]
  pub fn post_image(&self) -> Option<Image<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<Image<'a>>>(BoundingBoxes::VT_POST_IMAGE, None)
  }
  #[inline]
  pub fn boxes(&self) -> Option<&'a [Box]> {
    self._tab.get::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<Box>>>(BoundingBoxes::VT_BOXES, None).map(|v| v.safe_slice() )
  }
  #[inline]
  pub fn event_type(&self) -> PluginEvent {
    self._tab.get::<PluginEvent>(BoundingBoxes::VT_EVENT_TYPE, Some(PluginEvent::bounding_box_predict)).unwrap()
  }
}

pub struct BoundingBoxesArgs<'a> {
    pub ts: u32,
    pub original_image: Option<flatbuffers::WIPOffset<Image<'a >>>,
    pub post_image: Option<flatbuffers::WIPOffset<Image<'a >>>,
    pub boxes: Option<flatbuffers::WIPOffset<flatbuffers::Vector<'a , Box>>>,
    pub event_type: PluginEvent,
}
impl<'a> Default for BoundingBoxesArgs<'a> {
    #[inline]
    fn default() -> Self {
        BoundingBoxesArgs {
            ts: 0,
            original_image: None,
            post_image: None,
            boxes: None,
            event_type: PluginEvent::bounding_box_predict,
        }
    }
}
pub struct BoundingBoxesBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> BoundingBoxesBuilder<'a, 'b> {
  #[inline]
  pub fn add_ts(&mut self, ts: u32) {
    self.fbb_.push_slot::<u32>(BoundingBoxes::VT_TS, ts, 0);
  }
  #[inline]
  pub fn add_original_image(&mut self, original_image: flatbuffers::WIPOffset<Image<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<Image>>(BoundingBoxes::VT_ORIGINAL_IMAGE, original_image);
  }
  #[inline]
  pub fn add_post_image(&mut self, post_image: flatbuffers::WIPOffset<Image<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<Image>>(BoundingBoxes::VT_POST_IMAGE, post_image);
  }
  #[inline]
  pub fn add_boxes(&mut self, boxes: flatbuffers::WIPOffset<flatbuffers::Vector<'b , Box>>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(BoundingBoxes::VT_BOXES, boxes);
  }
  #[inline]
  pub fn add_event_type(&mut self, event_type: PluginEvent) {
    self.fbb_.push_slot::<PluginEvent>(BoundingBoxes::VT_EVENT_TYPE, event_type, PluginEvent::bounding_box_predict);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> BoundingBoxesBuilder<'a, 'b> {
    let start = _fbb.start_table();
    BoundingBoxesBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<BoundingBoxes<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

pub enum TelemetryMessageOffset {}
#[derive(Copy, Clone, Debug, PartialEq)]

pub struct TelemetryMessage<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for TelemetryMessage<'a> {
    type Inner = TelemetryMessage<'a>;
    #[inline]
    fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
        Self {
            _tab: flatbuffers::Table { buf: buf, loc: loc },
        }
    }
}

impl<'a> TelemetryMessage<'a> {
    #[inline]
    pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
        TelemetryMessage {
            _tab: table,
        }
    }
    #[allow(unused_mut)]
    pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
        _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
        args: &'args TelemetryMessageArgs) -> flatbuffers::WIPOffset<TelemetryMessage<'bldr>> {
      let mut builder = TelemetryMessageBuilder::new(_fbb);
      if let Some(x) = args.message { builder.add_message(x); }
      builder.add_message_type(args.message_type);
      builder.finish()
    }

    pub const VT_MESSAGE_TYPE: flatbuffers::VOffsetT = 4;
    pub const VT_MESSAGE: flatbuffers::VOffsetT = 6;

  #[inline]
  pub fn message_type(&self) -> MessageType {
    self._tab.get::<MessageType>(TelemetryMessage::VT_MESSAGE_TYPE, Some(MessageType::NONE)).unwrap()
  }
  #[inline]
  pub fn message(&self) -> Option<flatbuffers::Table<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<flatbuffers::Table<'a>>>(TelemetryMessage::VT_MESSAGE, None)
  }
  #[inline]
  #[allow(non_snake_case)]
  pub fn message_as_monitoring_frame_raw(&self) -> Option<MonitoringFrameRaw<'a>> {
    if self.message_type() == MessageType::MonitoringFrameRaw {
      self.message().map(|u| MonitoringFrameRaw::init_from_table(u))
    } else {
      None
    }
  }

  #[inline]
  #[allow(non_snake_case)]
  pub fn message_as_monitoring_frame_post(&self) -> Option<MonitoringFramePost<'a>> {
    if self.message_type() == MessageType::MonitoringFramePost {
      self.message().map(|u| MonitoringFramePost::init_from_table(u))
    } else {
      None
    }
  }

  #[inline]
  #[allow(non_snake_case)]
  pub fn message_as_bounding_boxes(&self) -> Option<BoundingBoxes<'a>> {
    if self.message_type() == MessageType::BoundingBoxes {
      self.message().map(|u| BoundingBoxes::init_from_table(u))
    } else {
      None
    }
  }

}

pub struct TelemetryMessageArgs {
    pub message_type: MessageType,
    pub message: Option<flatbuffers::WIPOffset<flatbuffers::UnionWIPOffset>>,
}
impl<'a> Default for TelemetryMessageArgs {
    #[inline]
    fn default() -> Self {
        TelemetryMessageArgs {
            message_type: MessageType::NONE,
            message: None,
        }
    }
}
pub struct TelemetryMessageBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> TelemetryMessageBuilder<'a, 'b> {
  #[inline]
  pub fn add_message_type(&mut self, message_type: MessageType) {
    self.fbb_.push_slot::<MessageType>(TelemetryMessage::VT_MESSAGE_TYPE, message_type, MessageType::NONE);
  }
  #[inline]
  pub fn add_message(&mut self, message: flatbuffers::WIPOffset<flatbuffers::UnionWIPOffset>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(TelemetryMessage::VT_MESSAGE, message);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> TelemetryMessageBuilder<'a, 'b> {
    let start = _fbb.start_table();
    TelemetryMessageBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<TelemetryMessage<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

#[inline]
pub fn get_root_as_telemetry_message<'a>(buf: &'a [u8]) -> TelemetryMessage<'a> {
  flatbuffers::get_root::<TelemetryMessage<'a>>(buf)
}

#[inline]
pub fn get_size_prefixed_root_as_telemetry_message<'a>(buf: &'a [u8]) -> TelemetryMessage<'a> {
  flatbuffers::get_size_prefixed_root::<TelemetryMessage<'a>>(buf)
}

#[inline]
pub fn finish_telemetry_message_buffer<'a, 'b>(
    fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>,
    root: flatbuffers::WIPOffset<TelemetryMessage<'a>>) {
  fbb.finish(root, None);
}

#[inline]
pub fn finish_size_prefixed_telemetry_message_buffer<'a, 'b>(fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>, root: flatbuffers::WIPOffset<TelemetryMessage<'a>>) {
  fbb.finish_size_prefixed(root, None);
}
}  // pub mod Telemetry
}  // pub mod PrintNannyMessage

